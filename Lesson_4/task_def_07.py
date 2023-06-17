def func(positional_only_parameters, /, positional_or_keyword_parameters, *,
keyword_only_parameters):
    pass

def standard_arg(arg):
    print(arg)

standard_arg(42)
standard_arg(arg=42)

def standard_arg_2(arg, /):
    print(arg)
standard_arg_2(42)
#standard_arg_2(arg=42)

def kwd_onle_arg(*, arg):
    print(arg)

#kwd_onle_arg(42)
kwd_onle_arg(arg=42)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only) 

#combined_example(1,2,3)
combined_example(1,2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)