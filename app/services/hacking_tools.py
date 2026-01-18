import subprocess

def run_hacking_tool(tool, args):
    try:
        result = subprocess.run([tool] + args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
