class RegionCounter:
    def __init__(self, regions):
        self.regions = regions  # List of tuples: [(region_name, (x1, y1, x2, y2)), ...]
        self.counts = {name: 0 for name, _ in regions}
        self.tracked_ids = set()

    def update(self, object_id, bbox):
        x_center = (bbox[0] + bbox[2]) // 2
        y_center = (bbox[1] + bbox[3]) // 2
        for name, (x1, y1, x2, y2) in self.regions:
            if x1 <= x_center <= x2 and y1 <= y_center <= y2:
                if object_id not in self.tracked_ids:
                    self.counts[name] += 1
                    self.tracked_ids.add(object_id)
