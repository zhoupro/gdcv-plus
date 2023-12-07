""" 查询单词
Usage:
      gdcv.py  --wd=<wd> 
"""

from docopt import docopt
import os
import hunspell

def queryWd(wd):
    hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
    wds = hobj.stem(wd)
    if (len(wds)==0):
        print("no")
        return
    for wd in wds:
        cmdstr = "/usr/local/bin/gdcv " + str(wd, encoding="utf-8")  +  " |sed -r 's/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g' |  grep -o 'BrE *\[[^.]*\]' |sed 's#BrE##g' | head -n 1"
        outwd=get_shell_result(cmdstr)
        if (len(outwd)>0):
            print(outwd)
            break


def get_shell_result(cmd):
    import subprocess
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    stdout = str(stdout, encoding="utf-8")
    stdout = stdout.strip().replace('[','/').replace(']','/')
    return stdout 

if __name__ == '__main__':
    arguments = docopt(__doc__.format(filename=os.path.basename(__file__)))
    queryWd(arguments["--wd"])

