FROM justb4/jmeter

COPY test-plan.jmx /test-plan.jmx

CMD ["jmeter", "-n", "-t", "/test-plan.jmx", "-l", "/test-result.log"]
