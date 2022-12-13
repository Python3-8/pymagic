# PyMagic

## Getting started

To download and set up PyMagic, open a terminal or command prompt window and type the following:

```sh
$ git clone git://github.com/Python3-8/pymagic.git  # downloads PyMagic
$ cd pymagic  # enters the PyMagic directory
$ python3 -m pip install -r requirements.txt  # installs the dependencies that PyMagic requires
```

Now you are ready to run PyMagic. This can be done by executing the following from the same window, in the same directory:

```sh
$ python3 main.py
```

## Using PyMagic

If you have run PyMagic with `python3 main.py`, you will now see this window:

![Welcome screen](https://user-images.githubusercontent.com/66139317/207399196-125a62c3-e00e-400f-a9ac-121a17e96c43.png)

If it is your first time using PyMagic, click the <kbd>Instructions</kbd> button to learn how to use PyMagic. Otherwise, click <kbd>Skip</kbd>. If you clicked
<kbd>Instructions</kbd>, you will now see this:

![Instructions](https://user-images.githubusercontent.com/66139317/207399497-88f58f93-6a29-46e2-a533-4bc4f970fbf0.png)

This shows how to use PyMagic. You will be presented with a blackboard which can be turned into a whiteboard and back by pressing <kbd>X</kbd>.
Think of this like a blackboard with you holding a piece of chalk or a whiteboard with you holding a dry-erase marker. Of course, if you move the
chalk or the marker (the tool), nothing happens, because the tool is not in contact with the board. Pressing <kbd>Q</kbd> or the left mouse button
places the tool on the board so that any movements will translate onto the board. For example, if you press <kbd>Q</kbd> and move the mouse pointer
in a straight line on your trackpad, a line will be drawn on the board. You do not have to press and hold anything. The left <kbd>Shift</kbd> key
changes the tool from a pen to an eraser and vice versa. The up and down arrow keys can be used to increase or decrease the tool thickness. Pressing
the <kbd>R</kbd> key sets the pen color to red. Similarly, <kbd>O</kbd> is orange, <kbd>Y</kbd> is yellow, <kbd>G</kbd> is green, <kbd>B</kbd> is blue,
<kbd>V</kbd> is purple, <kbd>P</kbd> is pink, <kbd>W</kbd> is white, and <kbd>Z</kbd> is black. After reading and learning these keys, click
<kbd>OK</kbd>.

Whether you clicked <kbd>OK</kbd> after reading the instructions or skipped them, you will now be presented with a blackboard.

![Blackboard](https://user-images.githubusercontent.com/66139317/207402368-02ab4d62-a0f7-47b6-80a7-c5010f142457.png)

Use your knowledge of the keys to draw or write, and enjoy!

## Note

You may realize while using PyMagic that the window snaps to specific sizes when resized. This is because the window has been programmed to always
be a golden rectangle (one whose length to width ratio is 1:ϕ, or 1:(1+√5)÷2, or approximately 1:1.618) to best resemble a physical whiteboard or blackboard.
