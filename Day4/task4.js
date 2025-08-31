var canfly = confirm('Do you fly?');

if (canfly) {
    var wildb1 = confirm('Are you wild?');
    if (wildb1) {
        document.writeln('then Eagle');
    } else {
        document.writeln('then Parrot');
    }
} else {
    var undersea = confirm('Do you live undersea?');
    if (undersea) {
        var wildb2 = confirm('Are you wild?');
        if (wildb2) {
            document.writeln('then Shark');
        } else {
            document.writeln('then Dolphin');
        }
    } else {
        var wildb3 = confirm('Are you wild?');
        if (wildb3) {
            document.writeln('then Lion');
        } else {
            document.writeln('then Cat');
        }
    }
}