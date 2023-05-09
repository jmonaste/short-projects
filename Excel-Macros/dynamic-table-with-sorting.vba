Sub CreatePivotTable()
    Dim sheetName As String
    Dim dataRange As Range
    Dim pivotTableName As String
    Dim pivotTableRange As String
    Dim tdSheet As Worksheet
    
    sheetName = "Sheet1" 'nombre de la hoja donde se encuentra la tabla de datos
    pivotTableName = "Tabla dinámica1" 'nombre de la tabla dinámica
    
    Set dataRange = Sheets(sheetName).Range("A2").CurrentRegion
    
    'Crear o limpiar hoja TD
    On Error Resume Next
    Set tdSheet = Sheets("TD")
    On Error GoTo 0
    If tdSheet Is Nothing Then
        Set tdSheet = Sheets.Add(After:=Sheets(Sheets.Count))
        tdSheet.Name = "TD"
    Else
        tdSheet.Cells.Clear
    End If
    
    'crear tabla dinámica
    pivotTableRange = "'" & sheetName & "'!" & dataRange.Address(ReferenceStyle:=xlR1C1)
    With tdSheet.PivotTableWizard(SourceType:=xlDatabase, SourceData:=pivotTableRange, TableDestination:=tdSheet.Range("A1"))
        
        tdSheet.PivotTables(1).Name = pivotTableName 'asignar nombre a la tabla dinámica
        
        With ActiveSheet.PivotTables(1).PivotFields("Material")
            .Orientation = xlRowField
            .Position = 1
        End With
        
        With ActiveSheet.PivotTables(1).PivotFields("Netvalue item")
            .Orientation = xlDataField
            .Function = xlSum
            .NumberFormat = "#,##0"
            .Name = "Netvalue item sum"
        End With
        
        With ActiveSheet.PivotTables(1).PivotFields("Document number")
            .Orientation = xlDataField
            .Function = xlCount
            .NumberFormat = "#,##0"
            .Name = "Document number count"
        End With
        
        'Format Pivot
        ActiveSheet.PivotTables(1).ShowTableStyleRowStripes = True
        ActiveSheet.PivotTables(1).TableStyle2 = "PivotStyleMedium9"
        
        With ActiveSheet.PivotTables(1).DataPivotField
            .Orientation = xlColumnField
            .Position = 1
        End With
        
        ' Ordenar por campo Netvalue
        ActiveSheet.PivotTables(1).PivotFields("Material").AutoSort _
        xlDescending, "Netvalue item sum", ActiveSheet.PivotTables(1). _
        PivotColumnAxis.PivotLines(1), 1
        
        
    End With
End Sub

