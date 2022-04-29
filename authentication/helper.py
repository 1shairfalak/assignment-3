class response_object:
    def __init__(self):
        self.data={}
        self.success=""
        self.error=""
        self.type=""
        self.heading=""
        self.show=""
        self.autohide=""
        self.description=""
    def set_response(self,data={},success="",error="",type="error",heading="Error",autohide=False,description="",show=True):
        self.data=data
        self.success=success
        self.error=error
        self.type=type
        self.show=show
        self.heading=heading
        self.description=description
        self.autohide=autohide;
    def get_response(self):
        return {"data":self.data,"message":{"type":self.type,"show":self.show,"autoHide":self.autohide,'heading':self.heading,"description":self.description}}




