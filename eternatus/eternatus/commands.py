from . import function

command_flag = ["-c", "-t", "-h", "--timer", "--clear", "--help"]
command_list = {
    "init": function.init,
    "run": function.run,
    "show_info": function.show_info,
    "watch": function.watch_and_run,
}
