use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn format_str(src: String) -> PyResult<String> {
    let mut buf = Vec::new();
    let mut config = ::rustfmt::config::Config::default();
    let mut session = ::rustfmt::Session::new(config, Some(&mut buf));
    let mut config = Config::default();
    config.set().edition(Edition::Edition2018);
    config.set().emit_mode(EmitMode::Stdout);

    session.format(::rustfmt::Input::Text(src)).unwrap();
    // ::rustfmt::format_input(
    //     ::rustfmt::Input::Text(src.clone()),
    //     &::rustfmt::config::Config::default(),
    //     Some(&mut buf),
    // );
    Ok(String::from_utf8(buf)?)
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn rustfmt_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(format_str, m)?)?;
    Ok(())
}
