class BrowserHistory:
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.index = 0
    def visit(self, url: str) -> None: 
        for i in range(len(self.stack) - self.index - 1):
            self.stack.pop()
        self.stack.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        newIndex = self.index - steps
        if newIndex < 0:
            newIndex = 0
        self.index = newIndex
        return self.stack[self.index]   

    def forward(self, steps: int) -> str:
        newIndex = self.index + steps
        if newIndex >= len(self.stack):
            newIndex = len(self.stack) - 1
        self.index = newIndex
        return self.stack[self.index]