from prompt_toolkit.application import Application
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import Float, HSplit, VSplit
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import (
    Box,
    Button,
    Checkbox,
    Dialog,
    Frame,
    Label,
    MenuContainer,
    MenuItem,
    ProgressBar,
    RadioList,
    TextArea,
)
from prompt_toolkit.key_binding import KeyBindings
from pygments.lexers.html import HtmlLexer
from prompt_toolkit.lexers import PygmentsLexer

import os
from git import Repo
from pydriller import RepositoryMining

print(os.path.dirname(os.path.realpath(__file__)))
repo = Repo(os.path.dirname(os.path.realpath(__file__)))


def get_untracked_files():
    return repo.untracked_files

textfield = TextArea(lexer=PygmentsLexer(HtmlLexer))

checkboxes = []
for item in get_untracked_files():
    checkboxes.append(Checkbox(text=item))

checkbox1 = Checkbox(text="Checkbox")
checkbox2 = Checkbox(text="Checkbox")

# commits_list = list(repo.iter_commits())
# print(f"First commit: {commits_list[0]}")

# changed_files = []
# changed_text = []
 
# for x in commits_list[0].diff(commits_list[-1]):
#     if x.a_blob.path not in changed_files:
#         changed_files.append(x.a_blob.path)
#         changed_text.append(x.a_blob.data_stream)
        
#     if x.b_blob is not None and x.b_blob.path not in changed_files:
#         changed_files.append(x.b_blob.path)
#         changed_text.append(x.b_blob.data_stream)
        
# print(changed_files)
# print(changed_files)

for item in repo.index.diff(None):
    import pdb;pdb.set_trace()
    print(item.a_path)

for commit in RepositoryMining(os.path.dirname(os.path.realpath(__file__)), only_in_branch=repo.active_branch.name).traverse_commits():
    for modified_file in commit.modifications:
        modfile = modified_file.filename
        # print(modified_file.diff)

def repobranchestolist(listobj):
    repoList = []
    for branch in listobj:
        repoList.append(branch.name)

    return repoList

repoList = repobranchestolist(repo.branches)
newrepoList = list(zip(repoList, repoList))
print(newrepoList)
radios = RadioList(newrepoList)
# radios = RadioList(
#     values=[
#         ("Red", "red"),
#         ("Green", "green"),
#         ("Blue", "blue"),
#         ("Orange", "orange"),
#         ("Yellow", "yellow"),
#         ("Purple", "Purple"),
#         ("Brown", "Brown"),
#     ]
# )
# radios = RadioList(repo.branches)

command_container = TextArea(text="Hello There", multiline=False)
commandWindowFrame= Frame(command_container,title="KubeTerminal (Ctrl-d to describe pod, Ctrl-l to show logs, Esc to exit, Tab to switch focus and refresh UI, 'help' for help)",height=4)

outputArea = TextArea(text="Ok There",
                      read_only=True)
outputAreaFrame = Frame(outputArea, title="Output")

output2Area = TextArea(text="Ok There 2",
                      read_only=True)
output2AreaFrame = Frame(output2Area, title="Output 2")


podListArea = TextArea(text="List",
                multiline=True,
                wrap_lines=False,
                read_only=True
                )
podListWindowSize=80
namespaceWindowSize=27
nodeWindowSize=53
podListAreaFrame = Frame(podListArea,title="Pods",width=podListWindowSize)

#content windows
# namespaceWindow = HSplit([checkbox1, checkbox2,])
namespaceWindow = HSplit(checkboxes)
namespaceWindowFrame= Frame(namespaceWindow,title="Namespaces",height=8)#,width=namespaceWindowSize)

nodeListArea = radios
nodeWindowFrame= Frame(nodeListArea,title="Nodes",height=8)#,width=nodeWindowSize)



upper_left_container = HSplit([namespaceWindowFrame,
                #HorizontalLine(),
                #Window(height=1, char='-'),
                nodeWindowFrame
                               ])


# upper_left_container = VSplit(
#     [
#         HSplit(
#             [
#                 Frame(body=ProgressBar(), title="Progress bar"),
#                 Frame(title="Checkbox list", body=HSplit([checkbox1, checkbox2,])),
#                 Frame(title="Radio list", body=radios),
#             ],
#             padding=1,
#         ),
#         HSplit(
#             [
#                 Frame(body=Label(text="Left frame\ncontent")),
#                 Dialog(title="The custom window", body=Label("hello\ntest")),
#                 textfield,
#             ],
#             height=D(),
#         ),
#
#     ]
# )

left_container = HSplit([upper_left_container,
                #HorizontalLine(),
                #Window(height=1, char='-'),
                podListAreaFrame],padding=1)

right_container = HSplit([outputAreaFrame,
    output2AreaFrame])

content_container = VSplit([
    # One window that holds the BufferControl with the default buffer on
    # the left.
    left_container,
    # A vertical line in the middle. We explicitly specify the width, to
    # make sure that the layout engine will not try to divide the whole
    # width by three for all these windows. The window will simply fill its
    # content by repeating this character.
    # VerticalLine(),
    # Window(width=1, char='|')

    # Display the text 'Hello world' on the right.
    # Window(content=FormattedTextControl(text='Hello world, Escape to Quit'))
    right_container

])


# 2. Key bindings
kb = KeyBindings()
kb.add("tab")(focus_next)
kb.add("s-tab")(focus_previous)
@kb.add("q")
def _(event):
    " Quit application. "
    event.app.exit()

root_container = HSplit([content_container,
     #           HorizontalLine(),
                #Window(height=1, char='-'),
                commandWindowFrame])


application = Application(
    layout=Layout(root_container),
    key_bindings=kb,
    mouse_support=True,
    full_screen=True,
)


def run():
    result = application.run()
    print("You said: %r" % result)


if __name__ == "__main__":
    run()
