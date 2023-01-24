import subprocess
import time
c = time.time()


runProc = subprocess.Popen(
    args=["python", 'test.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

print(runProc.returncode)
# grep_stdout = runProc.communicate(input="")[0]


print("Done", time.time() - c)
