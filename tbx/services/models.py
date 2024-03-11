from tbx.core.utils.fields import StreamField
from tbx.core.utils.models import ColourThemeMixin, SocialFields
from tbx.people.models import ContactMixin
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from .blocks import ServiceStoryBlock


class ServicePage(ColourThemeMixin, ContactMixin, SocialFields, Page):
    template = "patterns/pages/service/service_page.html"

    intro = RichTextField(blank=True)
    body = StreamField(ServiceStoryBlock(), use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    promote_panels = (
        [
            MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ]
        + ColourThemeMixin.promote_panels
        + ContactMixin.promote_panels
        + [
            MultiFieldPanel(SocialFields.promote_panels, "Social fields"),
        ]
    )

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]
