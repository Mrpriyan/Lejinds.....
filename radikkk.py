Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================= RESTART: E:\radik\pong.py =========================
Traceback (most recent call last):
  File "E:\radik\pong.py", line 74, in <module>
    ball.setx(ball.xcor() + ball.dx)
  File "C:\Users\User\AppData\Local\Programs\Python\Python37-32\lib\turtle.py", line 1808, in setx
    self._goto(Vec2D(x, self._position[1]))
  File "C:\Users\User\AppData\Local\Programs\Python\Python37-32\lib\turtle.py", line 3158, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\User\AppData\Local\Programs\Python\Python37-32\lib\turtle.py", line 755, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\User\AppData\Local\Programs\Python\Python37-32\lib\tkinter\__init__.py", line 2469, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
