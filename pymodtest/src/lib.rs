use pyo3::prelude::*;

#[pyfunction]
fn add_two(num: i64) -> i64 {
    // 2を足す関数
    num + 2
}


#[pymodule]
fn pymodtest(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_two, m)?)?;
    Ok(())
}
