class DashboardPage:
    def __init__(self,page):
        self.page = page

        self.search = page.get_by_placeholder("Search")
        self.Admin = page.get_by_role("link",name="Admin")

    def Admin_click(self):
        self.Admin.click()

        # self.PIM = page.get_by_role("link","PIM")
        # self.leave = page.get_by_role("link","Leave")
        # self.Time = page.get_by_role("link","Time")
        # self.Recruitment = page.get_by_role("link","Recruitment")
        # self.my_info = page.get_by_role("link","My Info")
        # self.performance = page.get_by_role("Link","Performance")
        # self.dashboard = page.get_by_role("Link","Dashboard")
        # self.directory = page.get_by_role("Link","Directory")
        # self.maintenance = page.get_by_role("Link","Maintenance")
        # self.claim = page.get_by_role("Link","Claim")
        # self.buzz = page.get_by_role("Link","Buzz")




        # def PIM(self):
        #     self.PIM.click()
        #
        # def leave(self):
        #     self.leave.click()
        #
        # def Time(self):
        #     self.Time.click()
        #
        # def Recruitment(self):
        #     self.Recruitment.click()