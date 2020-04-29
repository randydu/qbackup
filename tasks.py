from invoke import task

@task
def test(c):
    c.run('pytest')

@task
def run(c, gui=True):
    if gui:
        c.run('python -m qbackup')
    else:
        c.run('python -m qbackup.cli')