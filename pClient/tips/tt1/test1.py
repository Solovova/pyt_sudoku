from pywinauto import application

# app1 = application.Application().connect(title_re="SoloPri")
app = application.Application().connect(title="(SoloPri) Wurm Online 4.2.17(a01f324)")

# Wnd_Main = app.window(title_re="*SoloPri*Wurm")

lwin = app.windows

# for w in lwin:
print(len(lwin))

print(app)