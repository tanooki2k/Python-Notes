import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(access_level: str = 'admin'):  # Decorator to enforce user access level requirements
    """
        This is a flexible decorator used to enforce user access level requirements.

        Features:
         - Accepts a single parameter, which defines the required access level for a function.
         - Works with functions of any number of parameters.

        Usage:
         - Apply this decorator to functions that require restricted access based on user permissions.
    """

    def my_decorator(func):  # Inner function to wrap the target function with additional logic
        @functools.wraps(func)  # Preserves the original function's metadata
        def secure_func(*args, **kwargs):  # Wrapper function to check user's access level
            if user.get('access_level') == access_level:  # Check if the user has the required access level
                return func(*args, **kwargs)  # Call the original function if access is granted
            raise PermissionError(
                "User does not have the required permissions.")  # Raise an error if the user lacks required access

        return secure_func  # Return the wrapped function

    return my_decorator  # Return the decorator function


@user_has_permission()
def my_function(panel):
    """
    Allow us to retrieve the password for the admin panel.
    """
    return f'Password for {panel} panel is 1234.'


@user_has_permission()
def another():
    return 'Hello'


print(my_function.__name__)
print(another.__name__)

print(my_function('movies'))
print(another())
