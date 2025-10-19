#write functions here, don't add input('') statements here!
def test_config():
    return True

def use_global() -> int:
    """Increment the module-level global_counter and return the new value."""
    global global_counter
    global_counter += 1
    return global_counter