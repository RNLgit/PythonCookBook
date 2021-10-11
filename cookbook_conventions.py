"""
Description: Python conventions example
"""

__version__ = 0.1

CONSTANT_EXAMPLE = 0x1FFF


class ClassUseCamelCase:
    def __init__(self, variable):
        self.myself = variable
        self.__double_leading_underscore = 'attribute_1'

    def fcn_use_lowercase(self, fcn_var, timeout=1):
        """
        Doc string here
        """
        print(self.myself, fcn_var, timeout)
        raise ShowCaseError

    @staticmethod
    def static_fcn():
        print('This is static function')

    def _single_leading_underscore(self):
        print(self.__double_leading_underscore, 'weak internal use indicator')

    @classmethod
    def class_methods(cls, var1):
        print(var1)
        instance = cls('class methods showcase')
        print(instance.myself)


class ShowCaseError(Exception):
    """Show case of raise custom error"""
    pass


if __name__ == "__main__":
    show_instance = ClassUseCamelCase(123)

    try:
        show_instance.fcn_use_lowercase('var1')
    except ShowCaseError:
        print('show case error caught')

    show_instance.class_methods('class methods example')
