from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
import xlwt


def export_as_xls(modeladmin, request, queryset):
    """
    Generic xls export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('export')

    col = 0
    field_names = []
    # write header row
    for field in opts.fields:
        sheet.write(0, col, field.name)
        field_names.append(field.name)
        col = col + 1
    
    row = 1
    # Write data rows
    for obj in queryset:
        col = 0
        for field in field_names:
            val = unicode(getattr(obj, field)).strip()
            sheet.write(row, col, val)
            col = col + 1
        row = row + 1
    
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=admin_export.xls'
    book.save(response)
    return response
    
export_as_xls.short_description = "Export selected objects to XLS"