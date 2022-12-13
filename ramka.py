class BoundingBox:
    def __init__(self, bottom_left, upper_right):
        for a, b in zip(bottom_left, upper_right):
            if a < 0 or a > 1024:
                raise ValueError
            if b < 0 or b > 1024:
                raise ValueError
        self.bottom_left = tuple(bottom_left)
        self.upper_right = tuple(upper_right)

    def area(self):
        x1, y1 = self.bottom_left
        x2, y2 = self.upper_right
        return abs(x2-x1) * abs(y2-y1)

    def intersection_area(self, other: "BoundingBox"):
        p1_x1, p1_y1 = self.bottom_left  # lewy dolny p1
        p1_x2, p1_y2 = self.upper_right  # prawy górny p1
        p2_x1, p2_y1 = other.bottom_left  # lewy dolny p2
        p2_x2, p2_y2 = other.upper_right  # prawy górny p2
        if p1_x1 >= p2_x2 or p1_x2 <= p2_x1 or p1_y1 >= p2_y2 or p1_y2 <= p2_y1:
            return 0  # jeśli nie nachodzą pole wspólne to 0
        wsp_x1 = max(p1_x1, p2_x1)
        wsp_y1 = max(p1_y1, p2_y1)
        wsp_x2 = min(p1_x2, p2_x2)
        wsp_y2 = min(p1_y2, p2_y2)
        return (wsp_x2 - wsp_x1) * (wsp_y2 - wsp_y1)

    def union_area(self, other: "BoundingBox"):
        return self.area() + other.area() - self.intersection_area(other)

    def intersection_to_union_ratio(self, other: "BoundingBox"):
        return self.intersection_area(other) / self.union_area(other)

    def f1_coefficient(self, other: "BoundingBox"):
        return 2*self.intersection_area(other)/(self.area() + other.area())

    def __str__(self):
        x1, y1 = self.bottom_left
        x2, y2 = self.upper_right
        return f'x1: {x1}, y1: {y1}, x2: {x1}, y2: {y2}, x3: {x2}, y3: {y2}, x4: {x2}, y4: {y1}'
