while True:print(eval(input('>>>')))

# ⚠️ Limitations
# - Security Risk
# - eval() executes arbitrary Python code. If untrusted input is provided, it can run harmful commands (e.g., file deletion, system calls).
# - Example: __import__('os').system('rm -rf /') would execute a destructive shell command.
# - No Error Handling
# - Invalid expressions cause exceptions and crash the loop.
# - Example: entering open('file.txt') without proper handling will raise errors.
# - Infinite Loop
# - Runs forever until manually stopped. No built-in exit condition.
# - Limited Scope Control
# - By default, eval() uses the current global and local scope. Without restricting globals and locals, users can access or modify variables/functions unintentionally.
# - Not Suitable for Production
# - This REPL is only for experimentation or learning. Real interpreters use parsing, sandboxing, and safety checks.
