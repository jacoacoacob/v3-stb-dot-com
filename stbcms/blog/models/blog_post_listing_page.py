from wagtailseo.models import SeoMixin

from wagtail.models import Page

from .blog_post_page import BlogPostPage

class BlogPostListingPage(SeoMixin, Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = ["blog.BlogPostPage"]

  promote_panels = SeoMixin.seo_meta_panels + SeoMixin.seo_menu_panels

  def get_blog_posts(self):
    return BlogPostPage.objects.child_of(self).live()

  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    context["blog_posts"] = self.get_blog_posts()
    return context