from IPython.core.display import display_html as __display_html__


def __create_javascript_html__(*, is_hidden_by_default: bool = True) -> str:
    return """
            <script>
            // store the current state: hide or not
            code_hidden = {};
           """.format('false' if is_hidden_by_default else 'true') + \
           r"""
            function code_visibility_toggle() {
                if (code_hidden) {
                    $('div.input').show();
                } else {
                    $('div.input').hide();
                }
                code_hidden = !code_hidden
            } 
            
            // Invoke the function when the page is uploaded.
            // Thus, all the code cells are hidden by default.
            $( document ).ready(code_visibility_toggle);
            </script>
           """


def __create_message_html__() -> str:
    return '&#9757; ' \
           '<span style="color:gray; font-style: italic">' \
           'The code cells are hidden for better readability. ' \
           'To show them back or hide once again, click the button: </span>'


def __create_button_html__(button_text: str) -> str:
    return """<button onclick="javascript:code_visibility_toggle()">{}</button>
           """.format(button_text)


def hide_code_cells(*, message_text_html: str = __create_message_html__(),
                    button_text: str = 'Show/Hide Code Cells') -> None:
    """Hide all the code cells ('In[N]') in the notebook.

    The function create and invoke the javascript function that
    can hide or show code cells ('In[N]') in the given notebook.

    When the function is invoke the following happens:
      * all the code cells are hidden
      * a message explaining why the code cells are hidden
        and how they can be shown back is displayed
      * a button to hide/show the cells is displayed

    Arguments:
    message_text_html -- allows to redefine the default message
                         explaining why the code cells are hidden
    button_text       -- allows to change the text in the button
    """

    __display_html__(__create_javascript_html__(), raw=True)
    __display_html__(message_text_html + __create_button_html__(button_text), raw=True)


def create_button_to_hide_code_cells(*, message_text_html: str = __create_message_html__(),
                                     button_text: str = 'Show/Hide Code Cells') -> None:
    """Create a button to hide/show all the code cells ('In[N]') in the notebook.

    The function create the javascript function that can hide
    or show code cells ('In[N]') in the given notebook. It also
    creates a button to invoke the function (e.g., hide/show
    the code cells manually)

    When the function is invoke the following happens:
      * a message explaining why the code cells are hidden
        and how they can be shown back is displayed
      * a button to hide/show the cells is displayed

    Arguments:
    message_text_html -- allows to redefine the default message
                         explaining why the code cells are hidden
    button_text       -- allows to change the text in the button
    """

    __display_html__(__create_javascript_html__(is_hidden_by_default=False), raw=True)
    __display_html__(message_text_html + __create_button_html__(button_text), raw=True)
