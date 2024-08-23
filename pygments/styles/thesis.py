
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace

__all__ = ['ThesisStyle']

class ThesisStyle(Style):
    """
    Master thesis style (inspired by the BMW color scheme).
    """

    name = 'thesis'

    background_color = "#f8f8f8"

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #548D9E",
        Comment.Preproc:           "noitalic #9C6500",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #508130",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #AC1640",

        Operator:                  "#404040",
        Operator.Word:             "bold #AA22FF",

        Name.Builtin:              "#012C38",
        Name.Function:             "#012C38",
        Name.Class:                "bold #012C38",
        Name.Namespace:            "bold #012C38",
        Name.Exception:            "bold #AC1640",
        Name.Variable:             "#19177C",
        Name.Constant:             "#AC1640",
        Name.Label:                "#767600",
        Name.Entity:               "bold #717171",
        Name.Attribute:            "#687822",
        Name.Tag:                  "bold #012C38",
        Name.Decorator:            "#AA22FF",

        String:                    "#E96D0C",
        String.Doc:                "italic",
        String.Interpol:           "bold #A45A77",
        String.Escape:             "bold #AA5D1F",
        String.Regex:              "#A45A77",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#012C38",
        Number:                    "#404040",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#035970",
        Generic.Error:             "#E40000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.EmphStrong:        "bold italic",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#717171",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
