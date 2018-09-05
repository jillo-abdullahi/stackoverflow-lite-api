# app/utilities.py


def check_keys(args, length):
    """Function to check if dict keys are provided"""
    params = ['email', 'username', 'password', 'full-name']
    for key in args.keys():
        if key not in params or len(args) != length:
            return True
    return False


def check_empty_dict(args):
    """Function to check if an empty value's been given for any key"""
    for key in args:
        if not args[key].strip():
            return True
    return False
