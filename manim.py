from manimlib import *

def henon(x_n, y_n, alpha=1.4, beta=0.3, points=100, pointList=[], graph=True, outfile="henon.png"):
	for i in range(points):
		x_n1 = 1 - alpha * x_n * x_n + y_n
		y_n1 = beta * x_n
		pointList.append((x_n1, y_n1))
		x_n = x_n1
		y_n = y_n1
	return pointList

class CoordinateSystemExample(Scene):
	def construct(self):
		hr = henon(1, 1, points=10, graph=False)
		print("Generated Henon Mapping, Animating")
		L_X, L_Y = [[],[]]
		for x,y in hr:
			L_X.append(x)
			L_Y.append(y)
		self.cx = L_X
		self.cy = L_Y
		self.points = hr
		axes = Axes(
			x_range=(min(self.cx)-2, max(self.cx)+2),
			y_range=(min(self.cy)-2, max(self.cy)+2),
			axis_config={
				"stroke_color": BLUE,
				"stroke_width": 2,
			},
		)
	
		axes.add_coordinate_labels(
			font_size=10,
			num_decimal_places=1,
		)
		self.add(axes)

		dot = Dot(color=RED)
		dot.move_to(axes.c2p(
			self.points[0][0],
			self.points[0][1]
		))
		self.play(FadeIn(dot, scale=0.5))
		for p_i in range(1, len(self.points)):
			point = self.points[p_i]
			self.play(dot.animate.move_to(axes.c2p(point[0], point[1])), run_time=0.25)
			#self.wait()
			dotAfter = Dot(color=GREEN)
			dotAfter.move_to(axes.c2p(point[0], point[1]))
			self.play(FadeIn(dotAfter, scale=0.5),run_time=0.25)

		self.play(FadeOut(VGroup(axes, dot)))