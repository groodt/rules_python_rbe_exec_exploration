def _foo_impl(ctx):
    out = ctx.actions.declare_file(ctx.label.name)

    ctx.actions.run(
        executable = ctx.executable._foo_tool,
        arguments = [out.path],
        outputs = [out],
        inputs = [ctx.file.src],
    )
    return [DefaultInfo(files = depset([out]))]

foo = rule(
    implementation = _foo_impl,
    attrs = {
      "src": attr.label(allow_single_file = [".txt"]),
      "_foo_tool": attr.label(
          default = "//private:foo_tool",
          executable = True,
          cfg = "exec",
      ),
    },
)
