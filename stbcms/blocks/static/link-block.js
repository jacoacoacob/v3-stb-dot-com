function useFields(prefix, ...fieldNames) {
  return fieldNames.map((fieldName) => document.getElementById(`${prefix}-${fieldName}`));
}

function useWrappers(prefix, ...fieldNames) {
  return useFields(prefix, ...fieldNames.map((fieldName) => `${fieldName}-wrapper`))
}

function hide(element) {
  element.style.display = "none";
}

function show(element) {
  element.style.display = "inherit";
}

class LinkBlockDefinition extends window.wagtailStreamField.blocks.StructBlockDefinition {
  render(placeholder, prefix, initialState, initialError) {
    const block = super.render(
      placeholder,
      prefix,
      initialState,
      initialError
    );

    const [initialKind] = initialState.kind;

    const [kindField] = useFields(prefix, "kind");
    const [urlWrapper, pageWrapper] = useWrappers(prefix, "url", "page");

    const fieldVisibilityByLinkKind = {
      url() {
        hide(pageWrapper);
        show(urlWrapper);
      },
      page() {
        hide(urlWrapper);
        show(pageWrapper);
      }
    }

    fieldVisibilityByLinkKind[initialKind]()

    kindField.addEventListener("change", (event) => {
      fieldVisibilityByLinkKind[event.target.value]()
    });

    return block;
  }
}

window.telepath.register("blocks.models.LinkBlock", LinkBlockDefinition);