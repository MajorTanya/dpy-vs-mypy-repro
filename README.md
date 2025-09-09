update: checked this through all active versions of python (3.9-3.14rc1) and got errors in every one (but didn't check
if the message was identical but it looked very very similar at a glance).

to reproduce, install dependencies, then run mypy on `src`

```text
mypy src
```

outputs:

```text
example_cog.py:27: error: Argument 1 has incompatible type "Callable[[ExampleCog, Context[Bot]], Coroutine[Any, Any, None]]"; expected "Callable[[Never, Never, VarArg(Never), KwArg(Never)], Coroutine[Any, Any, Never]] | Callable[[Never, VarArg(Never), KwArg(Never)], Coroutine[Any, Any, Never]]"  [arg-type]                                                                                                                                                     
Found 1 error in 1 file (checked 1 source file)
```

discord.py github:
https://github.com/Rapptz/discord.py

discord.py docs:
https://discordpy.readthedocs.io/en/stable/

their hybrid command docs:
https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#hybrid-commands

hybrid command source:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/hybrid.py
