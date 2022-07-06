# # Problem Link https://leetcode.com/problems/design-browser-history/
#
class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.urls = self.urls[:self.current + 1]

        self.urls.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        if self.current - steps < 0:
            self.current = 0
        else:
            self.current -= steps

        return self.urls[self.current]

    def forward(self, steps: int) -> str:
        if steps + self.current >= len(self.urls):
            self.current = len(self.urls) - 1
        else:
            self.current += steps

        return self.urls[self.current]


browser_history = BrowserHistory('leetcode.com')
browser_history.visit('google.com')
browser_history.visit('facebook.com')
browser_history.visit('youtube.com')
browser_history.back(1)
browser_history.back(1)
browser_history.forward(1)
browser_history.visit('linkedin.com')
browser_history.forward(2)
browser_history.back(2)

print(browser_history.back(7))