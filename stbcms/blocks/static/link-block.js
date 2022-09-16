function useFields(prefix, ...fieldNames) {
  return fieldNames.map((fieldName) => document.getElementById(`${prefix}-${fieldName}`));
}

function useFieldWrappers(prefix, ...fieldNames) {
  return useFields(prefix, ...fieldNames).map((field, index) => {
    let parent = field.parentElement;
    while (parent) {
      parent = parent.parentElement;
      if (parent.dataset.contentpath === fieldNames[index]) {
        return parent;
      }
    }
    return parent;
  });
}

function markRequired(fieldWrapper, required) {
  let requiredMark = fieldWrapper.querySelector(".w-required-mark");
  if (!requiredMark) {
    requiredMark = document.createElement("span");
    requiredMark.classList.add("w-required-mark");
    requiredMark.textContent = "*";
    fieldWrapper.querySelector(".w-field__label").appendChild(requiredMark);
  }
  requiredMark.style.display = required ? "inline" : "none";
}

function hide(fieldWrapper) {
  fieldWrapper.style.display = "none";
}

function show(fieldWrapper) {
  fieldWrapper.style.display = "inherit";
}

class LinkBlockDefinition extends window.wagtailStreamField.blocks.StructBlockDefinition {
  render(placeholder, prefix, initialState, initialError) {
    const block = super.render(
      placeholder,
      prefix,
      initialState,
      initialError
    );

    const [initialKind] = initialState._kind;

    const [kindField] = useFields(prefix, "_kind");
    const [urlWrapper, pageWrapper, textWrapper] = useFieldWrappers(prefix, "_url", "_page", "_text");

    const fieldVisibilityByLinkKind = {
      URL() {
        hide(pageWrapper);
        show(urlWrapper);
        markRequired(pageWrapper, false);
        markRequired(urlWrapper, true);
        markRequired(textWrapper, true);
      },
      PAGE() {
        hide(urlWrapper);
        show(pageWrapper);
        markRequired(pageWrapper, true);
        markRequired(urlWrapper, false);
        markRequired(textWrapper, false);
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