func = lambda x: x
hooks = ["pre_pandoc","post_pandoc", "extend_options","post_make_bibliography"]
hooks = {k:func for k in hooks}