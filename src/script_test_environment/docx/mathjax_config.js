MathJax.Ajax.timeout = 1000;  // 1 second rather than 15 seconds
MathJax.Hub.Register.StartupHook("HTML-CSS Jax Startup",function () {
          MathJax.OutputJax["HTML-CSS"].Font.timeout = 500; // shorter than 5 second font timeout
});