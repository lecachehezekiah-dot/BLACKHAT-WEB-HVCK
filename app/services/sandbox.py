import e2b

def execute_in_sandbox(code):
    sandbox = e2b.Sandbox()
    result = sandbox.run(code)
    return result
