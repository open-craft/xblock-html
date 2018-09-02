import bleach


class Cleaner(bleach.Cleaner):  # pylint: disable=too-few-public-methods
    """
    This class will only help lowering the strictness level of `bleach.Cleaner` super class by redefining the safe
    values we're currently using and the prohibited ones.
    """
    def __init__(self, strict=True):
        """
        This is an override to the original bleaching cleaner, it deals with two bleaching modes, the strict mode,
        and the trusted mode.

        - Strict Mode (default): Mainly used for rendering strings that are not required to have too much attributes
          and tags and doesn't aloow the use of most of the styles attributes.
        - Trusted mode: Mainly used to render content that marked as trusted.

        :param strict: whether we should strictly process the text or not.
        """
        attributes = {
            'a': ['href', 'title', 'target', 'rel'],
            'span': ['style'],
            'p': ['style'],
            'ul': [],
            'img': ['src', 'alt', 'width', 'height'],
        }
        tags = [
            'a', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'span',
            'ol', 'strong', 'ul', 'p', 'img', 'pre', 'h3', 'h4', 'h5', 'h6'
        ]
        styles = ['font-family', 'text-align', 'color', 'text-decoration', 'padding-left', 'padding-right']

        if not strict:
            attributes.update({
                'abbr': ['title'],
            })
            attributes['ul'].append('style')
            attributes['img'].append('style')

            tags += ['h1', 'h2', 'script', 'sub', 'sup', 'div', 'abbr', 'iframe']

            styles += ['list-style-type', 'font-size', 'border-width', 'margin']

        self.styles = styles
        self.tags = tags
        self.attributes = attributes

        super(Cleaner, self).__init__(
            tags=self.tags,
            attributes=self.attributes,
            styles=self.styles,
            strip=True,
        )


class SanitizedText(object):  # pylint: disable=too-few-public-methods
    """
    This class is responsible for maintaining unsafe string values saved in the database. It returns a safe value of the
    passed text and an unsafe value if requested.
    """

    def __init__(self, value, strict=True):
        """
        This initializer takes a raw value that may contain unsafe content and produce a cleaned version of it. It's
        very helpful to maintain both versions of the content if we need to use it later as a Database field or so.
        :param value: The original string value that came from DB.
        :param strict: Whether to strictly process the given text or not.
        """
        cleaner = Cleaner(strict=strict)
        self.strict = strict
        self.adulterated_value = value
        self.sanitized_value = cleaner.clean(value)

    def _determine_values(self, other):
        """
        Return the values to be compared, if `other` is an instance of `str` then we will compare `other`'s value with
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
            raise TypeError('Unsupported operation between instances of \'{}\' and \'{}\''.format(
                type(self).__name__, type(other).__name__))

        return self_value, other_value

    def __str__(self):
        """
        :return: The value of the text depending on the strictness level.
        """
        return self.sanitized_value if self.strict else self.adulterated_value

    def __eq__(self, other):
        """
        :param other:
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value == other_value

    def __ne__(self, other):
        """
        :param other:
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value != other_value

    def __lt__(self, other):
        """
        :param other:
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value < other_value

    def __le__(self, other):
        """
        :param other:
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value <= other_value

    def __gt__(self, other):
        """
        :param other:
        :return: If the other is an instance of str, then this will
                 be compared to the clean value, otherwise, it'll
                 compare both objects regarding the original value.
        """
        other_value, self_value = self._determine_values(other)
        return self_value > other_value

    def __ge__(self, other):
        """
        :param other:
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
