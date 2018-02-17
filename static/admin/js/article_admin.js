django.jQuery(document).change(function()
{
    if (django.jQuery('#id_categorie option:selected').text() == "Jeux vidéos") {
        django.jQuery(".form-row.field-les_plus").show();
        django.jQuery(".form-row.field-les_moins").show();
    }
    else
    {
        django.jQuery(".form-row.field-les_plus").hide();
        django.jQuery(".form-row.field-les_moins").hide();
    }
})