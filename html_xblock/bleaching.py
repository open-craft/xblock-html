"""
A new HTML XBlock that is designed with security and embedding in mind.
"""
import bleach
from bleach.css_sanitizer import CSSSanitizer


class SanitizedText:  # pylint: disable=too-few-public-methods
    """
    This class is responsible for maintaining unsafe string values saved in the database.
    It returns a safe value of the passed text and an unsafe value if requested.
    """

    def __init__(self, value, allow_javascript=False):
        """
        This initializer takes a raw value that may contain unsafe content and produce a cleaned version of it.
        It's very helpful to maintain both versions of the content if we need to use it later as a Database field or so.
        :param value: The original string value that came from DB.
        :param allow_javascript: Whether to allow javascript via script tag.
        """
        self.allow_javascript = allow_javascript
        self.cleaner = self.get_cleaner()

        self.adulterated_value = value
        self.value = self.cleaner.clean(value)

    def get_cleaner(self):
        """
        This method will help lowering the strictness level of `bleach.Cleaner`.

        It does so by redefining the safe values we're currently using and
        considering safe in the platform.
        """
        # pylint: disable-next=unexpected-keyword-arg
        cleaner = bleach.Cleaner(
            tags=self._get_allowed_tags(),
            attributes=self._get_allowed_attributes(),
            css_sanitizer=CSSSanitizer(
                allowed_css_properties=self._get_allowed_styles()
            )
        )
        return cleaner

    def _get_allowed_tags(self):
        """
        This is an override to the original bleaching cleaner ALLOWED_TAGS.

        :return: Allowed tags depending on the bleaching mode
        """
        tags = bleach.ALLOWED_TAGS + [
            'br',
            'caption',
            'dd',
            'del',
            'div',
            'dl',
            'dt',
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'h6',
            'hr',
            'img',
            'p',
            'pre',
            's',
            'strike',
            'span',
            'sub',
            'sup',
            'table',
            'tbody',
            'td',
            'tfoot',
            'th',
            'thead',
            'tr',
            'u',
            'iframe',
        ]

        if self.allow_javascript:
            tags += ['script']

        return tags

    def _get_allowed_attributes(self):
        """
        This is an override to the original bleaching cleaner ALLOWED_ATTRIBUTES.

        :return: Allowed attributes depending on the bleaching mode
        """
        attributes = {
            '*': ['class', 'style', 'id'],
            'a': ['href', 'title', 'target', 'rel'],
            'abbr': ['title'],
            'acronym': ['title'],
            'audio': ['controls', 'autobuffer', 'autoplay', 'src'],
            'img': ['src', 'alt', 'title', 'width', 'height'],
            'table': ['class', 'style', 'border', 'cellspacing', 'cellpadding'],
            'tr': ['style'],
            'td': ['style', 'scope'],
        }

        return attributes

    def _get_allowed_styles(self):
        """
        This is an override to the original bleaching cleaner ALLOWED_STYLES.

        :return: Allowed styles depending on the bleaching mode
        """
        styles = [
            "azimuth",
            "background-color",
            "border-bottom-color",
            "border-collapse",
            "border-color",
            "border-left-color",
            "border-right-color",
            "border-top-color",
            "clear",
            "color",
            "cursor",
            "direction",
            "display",
            "elevation",
            "float",
            "font",
            "font-family",
            "font-size",
            "font-style",
            "font-variant",
            "font-weight",
            "height",
            "letter-spacing",
            "line-height",
            "overflow",
            "pause",
            "pause-after",
            "pause-before",
            "pitch",
            "pitch-range",
            "richness",
            "speak",
            "speak-header",
            "speak-numeral",
            "speak-punctuation",
            "speech-rate",
            "stress",
            "text-align",
            "text-decoration",
            "text-indent",
            "unicode-bidi",
            "vertical-align",
            "voice-family",
            "volume",
            "white-space",
            "width",
            'border',
            'border-style',
            'margin-left',
            'margin-right',
            'padding-left',
            'padding-right',
        ]

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
            self_value = self.value
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
        :return: The value of the text.
        """
        return self.value

    def __unicode__(self):
        """
        :return: The value of the text.
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
