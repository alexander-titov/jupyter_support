# -*- coding: utf-8 -*-
"""Functions to change default CSS style of tables in Jupter notebooks
"""

from IPython.display import display_html as __display_html__

__author__ = 'Alexander Titov'
__copyright__ = "Copyright 2017, Alexander Titov"
# __credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alexander Titov"
__email__ = "alexander.igorevich.titov@gmail.com"
__status__ = "Development"

# This style sets the left text alignment to all the elements.
#
# All the elements in a table body have white background and
# light gray borders.
#
# All the elements in a table header have light blue background
# and silver (close to gray) borders.
#
# Other parameters are the same as in the default Jupyter style
# for tables.
white_bg_gray_borders_style = """
<style>

/* The goal of this CSS file is to change the default
 * style of displaying pandas dataframes in Jupyter.
 *
 * Only style of objects inside tables of a certain class
 * are changed. The class is an external argument. By default,
 * all the pandas dataframe belong to "dataframe" class.
 *
 * In some cases, we have to use very odd CSS selectors.
 * For example:
 *     table.dataframe tr:only-child th:nth-child(n) {
 *         text-align: left;
 *     }
 *
 * You my ask, "Is it the same as the following code?":
 *     table.dataframe tr:only-child th {
 *         text-align: left;
 *     }
 *
 * In fact, yes. The problem is this selector exists
 * in Jupyter with another properties. In order to overwrite
 * it, we have to use more precise selectors, as they
 * have higher priority.
 *
 */

/* Set text alignment to the left everywhere
 */
table.dataframe table, table.dataframe thead,
table.dataframe tbody, table.dataframe tr,
table.dataframe td, table.dataframe th,
table.dataframe tr:only-child th:nth-child(n),
* {
    text-align: left;
}

/* Header
 */
table.dataframe th,
table.dataframe tr:only-child th:nth-child(n) {
    border: 1px solid Silver;
    background: Aliceblue;
}

/* Body
 */
table.dataframe table, table.dataframe thead,
table.dataframe tbody, table.dataframe tr,
table.dataframe td {
    border: 1px solid lightgray;
    background: white;
}

</style>
"""


def change_table_style(table_class: str = 'dataframe', table_style: str = None) -> None:
    """Change the default CSS style for displaying tables in Jupyter

    Change the default CSS style of all the tables belonging
    to a certain CSS class in a Jupyter notebook.

    Args:
        table_class: The first parameter. Defaults to 'dataframe'

            It defines a CSS class of tables that styles will be
            modified. The default value, 'dataframe', is equal
            to the default class of pandas dataframes.

            Note, it is assumed that all the CSS selectors in
            the `table_style` string starts from the 'table.dataframe'.
            When `table_class` is specified, its value replaces
            'dataframe' in the selectors.

        table_style: The second parameter. Defaults to None.

            A string containing the new CSS properties for
            tables. For example:

                table.class th {
                    text-align: left;
                }

            If is required that all the CSS selectors starts
            from the 'table.dataframe'. It guaranties that
            the properties will be applies to elements only
            inside tables.

            If it is not specified, style `white_bg_gray_borders_style`
            is used.

    Usage:
        * If you want to set the default style to all the pandas
          dataframes in your notebook, just invoke the function
          without arguments.

        * If you want to apply the new style only for certain
          tables, do the following.

          First, change the default tables class using `table_class`
          argument:
              change_tables_style(table_class='my_table_class')

          Then, add this class to the desired tables when you display
          them. For example, for pandas dataframes it can be
          done in the following way:
              from IPython.display import display_html
              display_html(
                  your_data_frame.to_html(classes='my_table_class'),
                  raw=True)
    """

    style = (table_style or white_bg_gray_borders_style)

    style.replace('table.dataframe', 'table.' + table_class)

    __display_html__(style, raw=True)
