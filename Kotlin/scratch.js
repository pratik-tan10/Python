var dict = {"R1":"1981 to 1991",
            "R2" : "1991 to 2001",
            "R3" : "2001 to 2011",
            "Ra" : "1981 to 2011"
}
var a = dict[$feature.WhenTime];
var b = $feature.V2D.toFixed(3);
Concatenate("Rate of population change of ",$feature.DISTRICT, " from ",a," was ",b," per year per 1000 thousand.")
Concatenate("Year : ",$feature.Years, " Population : ",$feature.Po2D)
Concatenate("Year : ",$feature.Years, " Population Density : ",$feature.PopDensity, " person per square Kilometers")
