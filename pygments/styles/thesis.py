

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
        Comment.Preproc:           "noitalic #EF6C00",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #DB3E34",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #8E24AA",

        Operator:                  "#4E4F50",
        Operator.Word:             "bold #6A1B9A",

        Name.Builtin:              "#AD3535",
        Name.Function:             "#8E24AA",
        Name.Class:                "bold #8E24AA",
        Name.Namespace:            "bold #8E24AA",
        Name.Exception:            "bold #8E24AA",
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#767600",
        Name.Entity:               "bold #4E4F50",
        Name.Attribute:            "#687822",
        Name.Tag:                  "bold #DB3E34",
        Name.Decorator:            "#AA22FF",

        String:                    "#0D47A1",
        String.Doc:                "italic",
        String.Interpol:           "bold #A45A77",
        String.Escape:             "bold #AA5D1F",
        String.Regex:              "#A45A77",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#008000",
        Number:                    "#4E4F50",

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
