import copy
import math
import json

shells = [
		{ "_id": 1, "value": 2, "remainingSpace": {"width": 12, "height": 4, "tall": 20} },
		{ "_id": 2, "value": 5, "remainingSpace": {"width": 12, "height": 6, "tall": 20} },
]

goods = [
	{ "_id": 1, "width": 2, "height": 2, "tall": 15, "quantity": 7, "value": 1, "rotated": False },
	{ "_id": 2, "width": 2, "height": 4, "tall": 10, "quantity": 3, "value": 2, "rotated": False },
	{ "_id": 3, "width": 3, "height": 2, "tall": 10, "quantity": 3, "value": 5, "rotated": False },
	{ "_id": 4, "width": 3, "height": 5, "tall": 25, "quantity": 3, "value": 1, "rotated": False },
]

def rotate(good):
	good["width"], good["height"] = good["height"], good["width"]

def get_min_area(g, s, rot=False):
	g = copy.deepcopy(g)

	if rot:
		rotate(g)

	column_capacity = s["remainingSpace"]["height"] // g["height"]

	placed_goods_per_column = min(column_capacity, g["quantity"])

	rows = g["quantity"] // placed_goods_per_column

	cols_used = math.ceil(g["quantity"] / placed_goods_per_column)

	return s["remainingSpace"]["height"] * cols_used * g["width"]

def placement(shells, goods):
	total_shells = []
	matrix = []
	tallGoods = []

	shs = copy.deepcopy(shells) # copy of dict
	gds = copy.deepcopy(goods)

	shs.sort(key=lambda x: x["value"], reverse=True)
	gds.sort(key=lambda x: x["value"] / (x["width"] * x["height"]), reverse=True)
	# print(" ".join(map(lambda x: str(x["value"]), goods)))

	for sh in shs:
		for g in gds:
			if g["tall"] > sh["remainingSpace"]["tall"]:
				tallGoods.append(g)
				continue

			is_fit = sh["remainingSpace"]["height"] >= g["height"] and sh["remainingSpace"]["width"] >= g["width"]
			is_fit_rotated = sh["remainingSpace"]["width"] >= g["height"] and sh["remainingSpace"]["height"] >= g["width"]

			if (is_fit or is_fit_rotated):

				if (is_fit and not is_fit_rotated):
					rot = False
				elif (not is_fit and is_fit_rotated):
					rot = True
				else:
					rot = get_min_area(g, sh, True) < get_min_area(g, sh)

				g["rotated"] = rot

				if rot:
					rotate(g)
				
				column_capacity = sh["remainingSpace"]["height"] // g["height"]
				placed_goods_per_column = min(column_capacity, g["quantity"])
				cols_used = math.ceil(g["quantity"] / placed_goods_per_column)

				for c in range(cols_used):
					x = len(matrix)
					matrix.append([{"_id": g["_id"], "good": g, "x": x, "y": c, "rotated": rot} if c + 1 <= g["quantity"] else {"_id": None} for c in range(column_capacity)])

					placed_goods_per_column = min(column_capacity, g["quantity"])
					g["quantity"] -= placed_goods_per_column

					sh["remainingSpace"]["width"] -= g["width"]

					# print(" ".join(map(lambda x: str(x[id]), matrix[-1])), rot)

					if (sh["remainingSpace"]["width"] <= 0):
						break

				# sh["remainingSpace"]["width"] -= cols_used * g["width"]

			else:
				print("Good with id = {} doesn't fit.".format(g["_id"]))

			if (sh["remainingSpace"]["width"] <= 0):
				break

		gds = [g for g in gds if g["quantity"] != 0]
		# matrix.append([])
		total_shells.append({"_id": sh["_id"], "matrix": matrix})
		print()

	total_shells.sort(key=lambda x: x["_id"])

	return json.dumps({"total_shells": total_shells, "tallGoods": tallGoods})

print(placement(shells, goods))

# for p in placement(shells, goods)["total_shells"]:
# 	print(p)

# return total_shells
# print(total_shells)

# for m in matrix:
# 	print(" ".join(map(lambda x: str(x[id]), m)))

# for g in goods:
# 	print(g)

# for t in total_shells:
# 	for k in t:
# 		for i in k:
# 			print(i, end=" ")
# 		print()
# 	print()