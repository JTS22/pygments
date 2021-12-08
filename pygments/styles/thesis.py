

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace

class ThesisStyle(Style):
    """
    Bachelor thesis style (inspired by the ACS color scheme).
    """

    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #4E4F50",
        Comment.Preproc:           "noitalic #DB9334",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #DB3E34",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #DB347C",

        Operator:                  "#4E4F50",
        Operator.Word:             "bold #B1005C",

        Name.Builtin:              "#DB3E34",
        Name.Function:             "#34D0DB",
        Name.Class:                "bold #34D0DB",
        Name.Namespace:            "bold #34D0DB",
        Name.Exception:            "bold #7D2313",
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#767600",
        Name.Entity:               "bold #717171",
        Name.Attribute:            "#687822",
        Name.Tag:                  "bold #008000",
        Name.Decorator:            "#AA22FF",

        String:                    "#EF9186",
        String.Doc:                "italic",
        String.Interpol:           "bold #A45A77",
        String.Escape:             "bold #AA5D1F",
        String.Regex:              "#A45A77",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#008000",
        Number:                    "#9D9EA0",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#008400",
        Generic.Error:             "#E40000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#717171",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
