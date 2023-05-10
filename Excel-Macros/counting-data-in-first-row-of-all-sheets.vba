
Sub macroContarDatos(nombreHoja As String)

    EliminarHojaTemporal
    
    Sheets(nombreHoja).Select
    Columns("A:A").Select
    Selection.Copy
    Set temporal = Sheets.Add(After:=ActiveSheet)
    temporal.Name = "temporal"
    

    Sheets("temporal").Select

    Columns("A:A").Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=True, Transpose:=False
    Columns("A:A").Select
    Application.CutCopyMode = False
    Selection.SpecialCells(xlCellTypeBlanks).Select
    Selection.EntireRow.Delete
    Columns("A:A").Select
    temporal.Move After:=Sheets(Sheets.Count) 'Movemos la nueva hoja al final
    
    ContarDatosColumnaA (nombreHoja)
    
End Sub




Sub EliminarHojaTemporal()
    Dim hojaTemporal As Worksheet
    
    On Error Resume Next 'Ignorar errores si la hoja no existe
    Set hojaTemporal = ThisWorkbook.Sheets("temporal")
    On Error GoTo 0 'Reactivar la gestión de errores
    
    If Not hojaTemporal Is Nothing Then
        Application.DisplayAlerts = False 'Desactivar los mensajes de alerta
        hojaTemporal.Delete 'Eliminar la hoja
        Application.DisplayAlerts = True 'Volver a activar los mensajes de alerta
    End If
End Sub

Sub ContarDatosColumnaA(nombreHoja As String)
    Dim hojaTemporal As Worksheet
    Dim ultimaFila As Long
    Dim contador As Long
    
    'Obtener la hoja "temporal"
    Set hojaTemporal = ThisWorkbook.Sheets("temporal")
    
    'Contar el número de datos en la columna A
    ultimaFila = hojaTemporal.Range("A" & Rows.Count).End(xlUp).Row
    contador = ultimaFila 'No restamos nada para contar todas las celdas con datos
    
    'Mostrar el resultado por pantalla
    MsgBox "Hay " & contador & " datos en la columna A de la hoja" & nombreHoja
End Sub

Sub EjecutarMacroEnTodasLasHojas()
    Dim hoja As Worksheet
    
    'Recorrer todas las hojas en el libro
    For Each hoja In ThisWorkbook.Sheets
        'Llamar a la macro "macroContarDatos" en la hoja actual
        macroContarDatos hoja.Name
    Next hoja
End Sub