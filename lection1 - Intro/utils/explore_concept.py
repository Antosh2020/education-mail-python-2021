import pluggy


hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")


class MySpec:

    @hookspec
    def myhook(self, arg1, arg2):
        ...


class Plugin1:

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin1.myhook")
        return arg1 + arg2


class Plugin2:

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin2.myhook")
        return arg1 - arg2


pm = pluggy.PluginManager("myproject")
pm.add_hookspecs(MySpec)

pm.register(Plugin1())
pm.register(Plugin2())

results = pm.hook.myhook(arg1=1, arg2=2)
print(results)
