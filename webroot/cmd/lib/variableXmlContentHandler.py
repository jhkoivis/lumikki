
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class variableXmlContentHandler(ContentHandler):
    """
    Usage Example:
        
        from xml.sax import make_parser
        parser = make_parser() 
        nameList = []
        curHandler = studentNamesHandler(nameList)
        parser.setContentHandler(curHandler) 
        parser.parse(open('testData/Osallistujat_Tfy-0.1011_20080909.xml'))
        print nameList
    """
    
    def __init__(self, configDict):
        """
        Init:
        - put nameList ot self.storage: this is the one where aal the names are put
        - init internal parameters (self.LastName = None and self.storage = False)
        """
        self.varName    = ""
        self.varValue   = "" 
        self.currentTag = None
        self.isVarName  = False
        self.isVarValue = False
        self.storage    = configDict
        
    def startElement(self, name, attrs): 
        """
        Parse student last names and add them to self.LastName
        """ 
        if name == 'var': 
            self.varName    = ""
            self.varValue   = ""
            self.isVarName  = False
            self.isVarValue = False
        if name == 'name':
            self.isVarName  = True
            self.isVarValue = False
        if name == 'value':
            self.isVarName  = False
            self.isVarValue = True
        return
    
    def characters (self, ch):
        """
        Reads data between <tag> </tag>, where "tag" 
        variable is defined in self.startElement
        """
        if self.isVarName:
            self.varName    += ch
        if self.isVarValue:
            self.varValue   += ch
        return
    
    def endElement(self, name):
        """
        Adds the parsed element to list given as a starting parameter.
        """
        if name == 'var':
            self.storage[self.varName.strip().encode('ascii')] = self.varValue.strip().encode('ascii')
        if name == 'name':
            self.isVarName  = False
            self.isVarValue = False
        if name == 'value':
            self.isVarName  = False
            self.isVarValue = False    
        
        return 
    
  
