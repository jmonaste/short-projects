Sub ObtenerCeldasCombinadasUltimaCelda()
    Dim ultimaCelda As Long
    Dim celda As Range
    Dim rangoCombinado As Range
    
    ultimaCelda = ActiveWorkbook.Worksheets("RO4").Range("A" & Rows.Count).End(xlUp).Row
    Set celda = ActiveWorkbook.Worksheets("RO4").Range("A" & ultimaCelda)
    
    If celda.MergeCells Then
        Set rangoCombinado = celda.MergeArea
        MsgBox "La última celda de la columna A está combinada con el rango " & rangoCombinado.Address & vbCrLf & _
               "La celda siguiente a la última celda combinada es la celda " & rangoCombinado.Offset(1, 0).Address
    Else
        MsgBox "La última celda de la columna A no está combinada."
    End If
End Sub