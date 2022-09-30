"""
A new HTML XBlock that is designed with security and embedding in mind.
"""
import bleach

try:
    from bleach.css_sanitizer import CSSSanitizer
except (ImportError, ModuleNotFoundError):
    # NOTE:
    # The bleach library changes the way CSS Styles are cleaned in
    # version 5.0.0. Since the edx-platform uses version 4.1.0 in
    # Maple, this import is handled within a try block.
    # This try block CAN BE REMOVED for Nutmeg
    CSSSanitizer = None


class SanitizedText:  # pylint: disable=too-few-public-methods
    """
    This class is responsible for maintaining unsafe string values saved in the database.
    It returns a safe value of the passed text and an unsafe value if requested.
    """

    def __init__(self, value, strict=True):
        """
        This initializer takes a raw value that may contain unsafe content and produce a cleaned version of it.
        It's very helpful to maintain both versions of the content if we need to use it later as a Database field or so.
        :param value: The original string value that came from DB.
        :param strict: Whether to strictly process the given text or not.
        """
        self.strict = strict
        self.cleaner = self.get_cleaner()

        self.adulterated_value = value
        self.sanitized_value = self.cleaner.clean(value)
        self.value = self.sanitized_value if self.strict else self.adulterated_value

    def get_cleaner(self):
        """
        This method will help lowering the strictness level of `bleach.Cleaner`.

        It does so by redefining the safe values we're currently using and
        considering safe in the platform.
        """
        if CSSSanitizer:
            # pylint: disable-next=unexpected-keyword-arg
            cleaner = bleach.Cleaner(
                tags=self._get_allowed_tags(),
                attributes=self._get_allowed_attributes(),
                css_sanitizer=CSSSanitizer(
                    allowed_css_properties=self._get_allowed_styles()
                )
            )
        else:
            # NOTE: This is maintaining backward compatibility with bleach 4.1.0
            # used in Maple release of edx-platform. This can be removed
            # for Nutmeg release which uses bleach 5.0.0
            # pylint: disable-next=unexpected-keyword-arg
            cleaner = bleach.Cleaner(
                tags=self._get_allowed_tags(),
                attributes=self._get_allowed_attributes(),
                styles=self._get_allowed_styles()
            )

        return cleaner

    def _get_allowed_tags(self):
        """
        This is an override to the original bleaching cleaner ALLOWED_TAGS.

        It deals with two bleaching modes: the strict mode, and the trusted mode.

        :return: Allowed tags depending on the bleaching mode
        """
        tags = [
            'a',
            'b',
            'blockquote',
            'code',
            'em',
            'h3',
            'h4',
            'h5',
            'h6',
            'i',
            'img',
            'li',
            'span',
            'strong',
            'pre',
            'ol',
            'ul',
            'p',
            'pre',
            'caption',
            'table',
            'thead',
            'tbody',
            'tfoot',
            'th',
            'tr',
            'td'
        ]

        if not self.strict:
            tags += ['h1', 'h2', 'script', 'sub', 'sup', 'div', 'abbr', 'iframe']

        return tags

    def _get_allowed_attributes(self):
        """
        This is an override to the original bleaching cleaner ALLOWED_ATTRIBUTES.

        It deals with two bleaching modes, the strict mode, and the trusted mode.

        :return: Allowed attributes depending on the bleaching mode
        """
        attributes = {
            'a': ['href', 'title', 'target', 'rel'],
            'img': ['src', 'alt', 'width', 'height'],
            'p': ['style'],
            'pre': ['class'],
            'span': ['style'],
            'ul': [],
            'table': ['class', 'style', 'border', 'cellspacing', 'cellpadding'],
            'tr': ['style'],
            'td': ['style', 'scope'],
        }

        if not self.strict:
            attributes.update({'abbr': ['title']})
            attributes['ul'].append('style')
            attributes['img'].append('style')

        return attributes

    def _get_allowed_styles(self):
        """
        This is an override to the original bleaching cleaner ALLOWED_STYLES.

        It deals with two bleaching modes, the strict mode, and the trusted mode.

        :return: Allowed styles depending on the bleaching mode
        """
        styles = [
            'background-color', 'border', 'border-collapse', 'border-color', 'border-style', 'color', 'font-family',
            'height', 'margin-left', 'margin-right', 'padding-left', 'padding-right', 'text-align', 'text-decoration',
            'vertical-align', 'width',
        ]

        if not self.strict:
            styles += ['list-style-type', 'font-size', 'border-width', 'margin']

        return styles

    def _determine_values(self, other):
        """
        Return the values to be compared.

        If `other` is an instance of `str` then we will compare `other`'s value with
        this instance's clean value. Else if `other` is an instance of this class we will compare the `other`'s
        adulterate value (The original value) with the instance adulterate value as well.
        :param other:
        :return: A tuple of values to be compared.
        """
        if isinstance(other, str):
            self_value = self.sanitized_value
            other_value = other
        elif isinstance(other, type(self)):
            self_value = self.adulterated_value
            other_value = other.adulterated_value
        else:
            raise TypeError(
                f'Unsupported operation between instances of \'{type(self).__name__}\' and \'{type(other).__name__}\''
            )

        return self_value, other_value

    def __str__(self):
        """
        :return: The value of the text depending on the strictness level.
        """
        return self.value

    def __unicode__(self):
        """
        :return: The value of the text depending on the strictness level.
        """
        return self.value

    def __eq__(self, other):
        """
        :param other: The object to compare with this object.
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value == other_value

    def __ne__(self, other):
        """
        :param other: The object to compare with this object.
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value != other_value

    def __lt__(self, other):
        """
        :param other: The object to compare with this object.
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value < other_value

    def __le__(self, other):
        """
        :param other: The object to compare with this object.
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value <= other_value

    def __gt__(self, other):
        """
        :param other: The object to compare with this object.
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value > other_value

    def __ge__(self, other):
        """
        :param other: The object to compare with this object.
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value >= other_value

    def __nonzero__(self):
        """
        :return: True if the adulterated_value contains a value, False otherwise.
        """
        return bool(self.adulterated_value)
