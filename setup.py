import cx_Freeze

executables = [cx_Freeze.Executable('racerboy.py')]

cx_Freeze.setup(
        name = "Racer Boy",
        options = {"build_exe": {"packages":["pygame"],  "include_files": ['racecar.png']}},
        executables = executables
        
        
        )