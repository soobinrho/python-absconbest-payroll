import os
from pylatex import Document, PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    LineBreak, NewPage, Tabularx, TextColor, simple_page_number
from pylatex.utils import bold, NoEscape
from absconbest_payroll.spreadsheetManipulation import *

#This module was 99% copy/pasted from PyLaTex's Documentation: https://jeltef.github.io/PyLaTeX/current/examples/complex_report.html

def generate_report(main_title, name, title, email, payroll):

    # For saving the report in the Desktop folder
    dir_data=os.path.join(
        '~',
        'Desktop',
        'absconbest_payroll',
        'data'
    )
    dir_data=os.path.expanduser(dir_data)
    dir_logo=os.path.join(
        dir_data,
        'logo.png'
    )

    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True
    }
    doc = Document(geometry_options=geometry_options)

    # Generating
    # first page style
    first_page = PageStyle("firstpage")

    # Header image
    with first_page.create(Head("L")) as header_left:
        with header_left.create(
            MiniPage(width=NoEscape(r"0.49\textwidth"), pos='c')
        ) as logo_wrapper:
            logo_file=dir_logo
            logo_wrapper.append(
                StandAloneGraphic(
                    image_options="width=120px",
                    filename=dir_logo
                )
            )

    # Add document title
    with first_page.create(Head("R")) as right_header:
        with right_header.create(MiniPage(
            width=NoEscape(r"0.49\textwidth"),
            pos='c',
            align='r')
        ) as title_wrapper:
            title_wrapper.append(LargeText(bold('Payroll Report')))
            title_wrapper.append(LineBreak())
            title_wrapper.append(MediumText(bold(main_title)))

    # Add footer
    with first_page.create(Foot("C")):
        first_page.append(simple_page_number())

    doc.preamble.append(first_page)

    #Add employee information
    with doc.create(Tabu("X[l] X[r]")) as first_page_table:
        employee = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='h')
        employee.append(name)
        employee.append("\n")
        employee.append(title)
        employee.append("\n")
        employee.append(email)

        #Dummy table
        branch = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='t!',
                          align='r')
        # branch.append(bold("1181..."))
        # branch.append(LineBreak())
        # branch.append(bold("TIB Cheque"))

        first_page_table.add_row([employee, branch])
        first_page_table.add_empty_row()

    doc.change_document_style("firstpage")
    doc.add_color(name="lightgray", model="gray", description="0.80")

    #Add payroll table
    with doc.create(LongTabu("X[l] X[c] X[c] X[c] X[r]",
                             row_height=1.5)) as data_table:
        data_table.add_row(['Work',
                            'Rate Per Hour ($)',
                            'Time in Minutes',
                            'Time in Hours',
                            'Wage ($)'],
                           mapper=bold,
                           color="lightgray")
        data_table.add_empty_row()
        data_table.add_hline()

        #Following Pandas' API
        payroll=payroll.reset_index()
        for i in range(len(payroll.index)):
            try:
                row = [payroll['Work'][i],
                       round(payroll['Rate Per Hour'][i],0),
                       round(payroll['TIM'][i],0),
                       round(payroll['TIH'][i],3),
                       round(payroll['Wage'][i],1)]
            except TypeError:
                row = [payroll['Work'][i],
                       'n/a',
                       round(payroll['TIM'][i],0),
                       round(payroll['TIH'][i],3),
                       round(payroll['Wage'][i],1)]
            if (i%2)==0:
                data_table.add_row(row, color="lightgray")
            else:
                data_table.add_row(row)
        # data_table.add_row([payroll['Work'][l_p],
        #                     round(payroll['TIM'][l_p],0),
        #                     round(payroll['TIH'][l_p],3),
        #                     '',
        #                     round(payroll['Wage'][l_p],1)]
        # )

    doc.append(NewPage())

    doc.generate_pdf(
        filepath=os.path.join(
dir_data,
            main_title.lower().replace(" ","_").replace(",",""),
        ),
        clean_tex=True,
        clean=True,
    )
