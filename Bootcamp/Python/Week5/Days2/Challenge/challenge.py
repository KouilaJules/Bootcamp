class Pagination:
    def __init__(self, items=None, pageSize=10):
        if items is None:
            items = []
        self.items = items
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = max(1, len(items) // self.pageSize + (len(items) % self.pageSize != 0))

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        self.currentPage = max(1, min(self.totalPages, pageNum))
        return self